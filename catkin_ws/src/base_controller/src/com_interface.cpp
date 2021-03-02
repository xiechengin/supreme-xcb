
#include "base_controller/com_interface.h"
#include <string.h>


ComListener::ComListener() {}

ComListener::~ComListener() {}

ComInterface::ComInterface(const char *name, int type) {
    device_fd_ = 0;
    status_ = -1;
    is_ready_ = false;
    last_error_ = 0;

    if (name == nullptr || strlen(name) == 0) {
        name_ = "ComInterface";
    } else {
        name_ = name;
    }
    type_ = type;
}

ComInterface::~ComInterface() {}

void ComInterface::AddListener(ComListener *listener) {
    if (listener != nullptr) {

        for (std::list<ComListener*>::iterator it = listener_.begin();
             it != listener_.end(); ++it) {
            if (*it == listener) {
                return;
            }
        }
        listener_.push_back(listener);
    }
}

void ComInterface::RemoveListener(ComListener *listener) {
    if (listener != nullptr) {

        for (std::list<ComListener*>::iterator it = listener_.begin();
             it != listener_.end(); ++it) {
            if (*it == listener) {
                it = listener_.erase(it);
                break;
            }
        }
    }
}
	
