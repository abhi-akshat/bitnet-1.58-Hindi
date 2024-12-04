# Use NVIDIA CUDA base image compatible with H100 and Ubuntu 22.04
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# Install essential system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    git \
    libjpeg-dev \
    libpng-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Set the working directory
WORKDIR /workspace

# Copy the requirements.txt file into the container
COPY . /workspace/

# Install Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure NVIDIA runtime is available
LABEL com.nvidia.volumes.needed="nvidia_driver"
LABEL com.nvidia.cuda.version="12.2"

# Expose default ports (if running Jupyter or other services)
EXPOSE 8888

# Default command to run in the container
CMD ["bash"]
