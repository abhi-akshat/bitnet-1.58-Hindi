FROM nvidia/cuda:12.0.1-devel-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/conda/bin:$PATH"

# Install essential dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    git \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy

# Update Conda and create a new Python environment
RUN conda update -n base -c defaults conda && \
    conda create -n python_env python=3.10 -y && \
    conda clean -a -y

# Activate the Python environment
SHELL ["conda", "run", "-n", "python_env", "/bin/bash", "-c"]

# Install Python libraries (example)
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /

# Default command to start the container
CMD ["conda", "run", "-n", "python_env", "bash"]
