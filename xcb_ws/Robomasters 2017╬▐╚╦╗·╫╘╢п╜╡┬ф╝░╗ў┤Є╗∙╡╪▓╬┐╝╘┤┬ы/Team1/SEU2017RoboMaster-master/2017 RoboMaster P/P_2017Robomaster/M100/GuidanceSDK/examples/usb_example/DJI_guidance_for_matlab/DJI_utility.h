#ifndef __DJI_UTILITY_H__
#define __DJI_UTILITY_H__
#include <stdio.h>

#ifdef WIN32

#include <Windows.h>
#include <WinBase.h>

class lock
{
public:
	lock();
	~lock();
	void         enter();
	void         leave();
private:
	CRITICAL_SECTION  m_critical_section;
};

class event
{
public:
	event();
	~event();
	int         set_event();
	int         wait_event();
private:
	HANDLE      m_pipe_read;
	HANDLE      m_pipe_write;
};

#else

#include <pthread.h>
#include <semaphore.h>

class lock
{
public:
	lock();
	~lock();
	void         enter();
	void         leave();
private:
	pthread_mutex_t m_lock;
};

class event
{
public:
	event();
	~event();
	int         set_event();
	int         wait_event();
private:
	sem_t		m_sem;
};

#endif

void   sleep( int microsecond );


#endif