#include "pch.h"
#include <iostream>
#include <thread>
#include <chrono>
#include <cstdio>
#include <stdint.h>
#include <string>
#ifdef _MSC_VER
# include <intrin.h>
#else
# include <x86intrin.h>
#endif


uint64_t get_cycles() {
	// _mm_lfence();  // optionally wait for earlier insns to retire before reading the clock
	uint64_t tsc = __rdtsc();
	// _mm_lfence();  // optionally block later instructions until rdtsc retires
	return tsc;
}

typedef std::chrono::duration<double, std::ratio<1, 1>> seconds_t;

const char* program_name;

auto start_time = std::chrono::high_resolution_clock::now();

double age()
{
	return seconds_t(std::chrono::high_resolution_clock::now() - start_time).count();
}

void PrintUsage()
{
	printf("Usage:\n");
	printf("%s [measurment duration]\n", program_name);
}

int main(int argc, char** argv)
{
	using namespace std::chrono_literals;
	program_name = argv[0];
	int sleeptime = 100;
	switch (argc) {
	case 1:
		sleeptime = 100;
		break;
	case 2:
		try
		{
			sleeptime = std::stoi(argv[1]);
		}
		catch (...)
		{
			printf("Error: argument was not an integer.");
			PrintUsage();
			return 1;
		}
		break;
	default:
		printf("Error: too many arguments.");
		PrintUsage();
		return 1;
		break;
	}
	uint64_t cycles_start = get_cycles();
	double time_start = age();
	std::this_thread::sleep_for(sleeptime * 1ms);
	uint64_t elapsed_cycles = get_cycles() - cycles_start;
	double elapsed_time = age() - time_start;
	printf("CPU MHz: %.3f\n", elapsed_cycles / elapsed_time / 1000000.0);

}